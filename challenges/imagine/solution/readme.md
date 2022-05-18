# Solution
We are given a file called `imagine_docker.tar`. This is an exported, built Docker image. The name should give it away here. A different approach is to look up e.g. `tar file manifest.json`. The file structure is quite unique and memorable.

The file can be loaded into your local registry by running `sudo docker image load -i ./imagine_docker.tar`. From here, you can use various tools and commands to inspect the image, as well as extract the `tar` archive and explore it manually. A Docker image consists of multiple layers. Each layer can be seen as a checkpoint in the setup process. Each layer corresponds with a line in the `Dockerfile` that was used to build the image.

`sudo docker history imagine` will show each layer in the loaded image. Looking in the `CREATED` column, the top 8 entries' creation dates differ from the lower ones. We can conclude that the youngest layers are the ones created by the end-developer, and the others are part of the used base Docker image. `docker history` will indicate `<missing>` for layer IDs, which is pretty annoying. Here is how you can manually map commands to layers:
1. Choose a command in `docker history`'s output that interests you.
2. Count its `index`.
    - youngest are on top of the list
3. Extract `imagine_docker.tar`.
4. Check the `manifest.json`, it contains all the layer IDs.
5. Count `index - 1` in the list of layer hashes. `-1` as the last layer is listed separately under `Config` in `manifest.json`.
    - count from the bottom here, as youngest are on the bottom of the list

After some digging, you should see that 2 `theme.zip` files are added to the image: one by `COPY`ing it in, and the other by downloading it. The one that is copied actually contains the flag.