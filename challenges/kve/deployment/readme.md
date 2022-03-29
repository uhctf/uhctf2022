# Deployment
1. Change the flag in `./src/device/custom/fix_emulation.sh`
2. Change the amount of instances in the `docker-compose.yml`
    1. each instance must be explicitly mentioned due to hardcoded IPs
    2. for each instance
        - set a unique port mapping
        - set a unique IP address
            - `TO_IP` must match `ipv4_address`
            - `TO_IP` and `TO_GATEWAY` must be in the subnet defined under `emulation_net`
            - `TO_IP` and `TO_GATEWAY` must be a maximum of 11 characters in length due to them being used in binary rewriting. Less may be padded with null-bytes (tho, this has not been tested).
3. Go to the `./src/` directory.
4. Execute `install.sh`
5. Execute `run.sh`
    - it may complain about not being able to connect to the database. Simple re-run the script till it works.