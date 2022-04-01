FROM fcore:latest

RUN apt-get update
RUN apt-get install -y flex
RUN apt-get --yes clean

# copy to ensure a "clean" emulation each time. Otherwise, edits in the emulation would persist between restart of the docker
COPY ./FirmAE/ /work/FirmAE/

COPY ./binary_rewrite/ /binary_rewrite/
WORKDIR /binary_rewrite/

# Binary rewrite IP
ARG IID
ARG FROM_IP
ARG TO_IP
ARG FROM_GATEWAY
ARG TO_GATEWAY
RUN ["sh", "-c", "/binary_rewrite/rewrite.sh /work/FirmAE/scratch/${IID}/ ${FROM_IP} ${TO_IP} ${FROM_GATEWAY} ${TO_GATEWAY}"]

# customisations for the emulated FW
COPY ./device/custom/ /work/custom/
WORKDIR /work/custom/
RUN ["sh", "-c", "/work/custom/gen_hook.sh"]
RUN ["sh", "-c", "echo -n ${TO_IP} > /work/custom/libnvram.override/lan_ipaddr"]
RUN sed -i "s/<gateway>/${TO_GATEWAY}/g" /work/custom/fix_emulation.sh

# used to emulate
ADD ./device/firmware.zip /work/firmwares/firmware.zip

# Actually run the emulation
WORKDIR /work/FirmAE/
CMD ["sh", "-c", "/work/FirmAE/run.sh -r ${BRAND} /work/firmwares/firmware.zip"]
