# Solution
This challenge presents the common modulus vulnerability of RSA. While IRL it should not appear, it is a neat theoretical problem serving as introduction to cryptography's math and modular arithmetic. The reason it does not appear IRL is that for this attack to succeed, no padding may be added to the cypher text. It is also highly unlikely that someone will send the same plain text multiple times with the same modulus but different exponents.

Asymmetric encryption of a message uses the public key to garble the message. In the case of RSA this is as simple as <code>Cyphertext = Message<sup>e</sup> mod N</code>. In other words, an RSA public key only consists of 2 parameters: an exponent and a modulus. We are given 2 public keys in PEM format. The PEM encoding and structure of these keys is interesting to look at. However, for now we simply only care about reading the 2 parameters from the keys. This can be done using `openssl rsa -inform PEM -pubin -text < key.pem`. Comparing the parameters found in the 2 keys, we notice that they share the same modulus but use different exponents. Researching this peculiar pattern should lead us to the common modulus vulnerability. You can either re-use existing solving scripts, there are plenty [online](https://gist.github.com/idarthjedi/1ab9c9ccd4803dbc40c801fbc5f2488f), or implement it yourself as the required math is not too complex and explained online.

Given that we accept a few more difficult theorems to be as they are, the actual math required to explain the common modulus attack is relatively simple. First we note the difference between `a = b mod N` and `c ≡ d (mod N)`. The prior divides `b` by `N` and returns the remainder. The latter states that `c` and `d` are congruent under modulo `N`. This means `c` and `d` are equal given that we apply the modulo to both of them. In other words, the remainder of dividing `c` by `N` is the same as the remainder of the division of `d` by `N`. Thus, the first equation applies the modulo to 1 side, while the other applies it globally/to both sides. Of course, the result (`a`) of `b mod N` is congruent with `b` itself due to how the modulus operator works. In other words, if `a = b mod N` then `a ≡ b (mod N)`. Or applied to RSA: <code>C ≡ M<sup>e</sup> (mod N)</code>.

The formula proving the common modulus attack requires 2 established pieces of theory: Bezout's Identity and the Extended Euclidean Algorithm (EEA). Bezout's Identity states that for some positive integers `a` and `b` it is possible to find a `u` and `v` such that below equation holds. The EEA can then be used to calculate `u`, `v`, and `gcd(a,b)` given `a` and `b`.
```
a*u + b*v = gcd(a,b)
```

Now, why is Bezout's Identity so interesting? It is because we can use it to simplify the mathematical equation built from the parameters available in our setup. Remember that while we have 2 cypher texts matching each public key, they both contain the same message/plain text. The equation looks as follows and can easily be simplified as shown:
<pre>
C<sub>1</sub><sup>u</sup> * C<sub>2</sub><sup>v</sup> ≡ (M<sup>e<sub>1</sub></sup>)<sup>u</sup> * (M<sup>e<sub>2</sub></sup>)<sup>v</sup>   (mod N)
         ≡ (M<sup>e<sub>1</sub>*u</sup>) * (M<sup>e<sub>2</sub>*v</sup>)  (mod N)
         ≡  M<sup>e<sub>1</sub>*u + e<sub>2</sub>*v</sup>      (mod N)
</pre>

Notice how the calculation in the exponent of `M` is similar to the left hand side of Bezout's Identity? Let's replace it!
<pre>
C<sub>1</sub><sup>u</sup> * C<sub>2</sub><sup>v</sup> ≡ M<sup>gcd(e<sub>1</sub>, e<sub>2</sub>)</sup> (mod N)
</pre>

Again, as modular arithmetic might be new for some, this is the same as:
<pre>
(C<sub>1</sub><sup>u</sup> * C<sub>2</sub><sup>v</sup>) mod N = M<sup>gcd(e<sub>1</sub>, e<sub>2</sub>)</sup> mod N
</pre>

Thus, we can calculate <code>M<sup>1</sup></code>, which is just our plain text, given a common modulus and 2 different exponents of which the `gcd` is 1. If we double check this constraint for the 2 given public keys we indeed see that `gcd(65537, 42337) = 1`.

Naively porting above formula to code will result in issues due to the size of the numbers being used. The calculation might overflow or simply stall. It is important to remember that all the calculations happen under the common modulo. In other words, instead of performing <code>(C<sub>1</sub><sup>u</sup> * C<sub>2</sub><sup>v</sup>) mod N</code> which would multiple 2 huge numbers before performing the modulo, we can take the modulo for each component and multiply afterwards <code>(C<sub>1</sub><sup>u</sup> mod N) * (C<sub>2</sub><sup>v</sup> mod N)</code>.