const no_letter_start = (password) => {
    return /^[^a-zA-Z]/.test(password);
}

const no_digit_end = (password) => {
    return /[^0-9]$/.test(password);
}

const contain_special = (password) => {
    return ((password).match(/[!$^*@]/gu) || []).length === 3;
}

const contain_digit = (password) => {
    // check digits in second half
    let amount_digits = 0;
    for (let i = Math.floor(password.length/2); i < password.length; i++) {
        if (password[i] >= '0' && password[i] <= '9'){
            amount_digits += 1;
        }
    }
    return amount_digits === 2;
}

const no_username_chars = (password, username) => {
    // check no characters from username
    for (let i = 0; i < username.length; i++) {
        if (password.indexOf(username[i]) !== -1) {
            return false;
        }
    }
    return true;
}

const no_whitespace = (password) => {
    return /[^\s]/.test(password);
}

const diff_categories = (password) => {
    // check consecutive characters from different categories
    let last_category = '';
    const allowed_specials = ['!', '$', '^', '*', '@'];
    for (let character of [...password]) {
        if (character >= '0' && character <= '9'
            && last_category !== 'number') {
                last_category = 'number';
        }
        else if ((character >= 'a' && character <= 'z' || character >= 'A' && character <= 'Z') && last_category !== 'letter') {
            last_category = 'letter';
        }else if (allowed_specials.indexOf(character) > -1 && last_category !== 'special') {
            last_category = 'special';
        }else {
            return false;
        }
    }
    return true;
}

const length_check = (password) => {
    // check length of password
    return password.match(/./gu).length === 8;
}

const password_policy_check = (username, password) => {
    try {
        return no_letter_start(password)
        && no_digit_end(password)
        && contain_special(password)
        && contain_digit(password)
        && no_username_chars(password, username)
        && no_whitespace(password)
        && diff_categories(password)
        && length_check(password);
     } catch (_) {
        return false;
    }
}

const password_policy_update = () => {
    try {
        const username = document.getElementById('name').value;
        const password = document.getElementById('password').value;

        if (no_letter_start(password)) {
            document.getElementById('no_letter_start').classList.add('na')
        }
        else {
            document.getElementById('no_letter_start').classList.remove('na');
        }

        if (no_digit_end(password)) {
            document.getElementById('no_digit_end').classList.add('na');
        }
        else {
            document.getElementById('no_digit_end').classList.remove('na');
        }

        if (contain_special(password)) {
            document.getElementById('contain_special').classList.add('na');
        }
        else {
            document.getElementById('contain_special').classList.remove('na');
        }

        if (contain_digit(password)) {
            document.getElementById('contain_digit').classList.add('na');
        }
        else {
            document.getElementById('contain_digit').classList.remove('na');
        }

        if (no_username_chars(password, username)) {
            document.getElementById('no_username_chars').classList.add('na');
        }
        else {
            document.getElementById('no_username_chars').classList.remove('na');
        }

        if (no_whitespace(password)) {
            document.getElementById('no_whitespace').classList.add('na');
        }
        else {
            document.getElementById('no_whitespace').classList.remove('na');
        }

        if (diff_categories(password)) {
            document.getElementById('diff_categories').classList.add('na');
        }
        else {
            document.getElementById('diff_categories').classList.remove('na');
        }

        if (length_check(password)) {
            document.getElementById('length_check').classList.add('na');
        }
        else {
            document.getElementById('length_check').classList.remove('na');
        }
    } catch (_) {
    }
};
