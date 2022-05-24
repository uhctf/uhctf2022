FROM python:3.9

# add root flag
ARG ROOT_FLAG='uhctf{real-hackers-live-off-the-land-a69c22}'
RUN echo ${ROOT_FLAG} > /root/flag.txt

# setup user
ARG USERNAME=webadmin
RUN apt-get update && apt-get install -y sudo && apt-get clean
RUN useradd -ms /bin/bash ${USERNAME}
RUN echo "${USERNAME} ALL=(ALL) NOPASSWD: /usr/bin/apt-get" >> /etc/sudoers
USER ${USERNAME}

# setup website
RUN mkdir -p /home/${USERNAME}/f2_website/
# Note: only the contents are copied
COPY ./src/ /home/${USERNAME}/f2_website/
WORKDIR /home/${USERNAME}/f2_website/
RUN pip install --no-cache-dir -r ./requirements.txt

# add user flag
ARG USER_FLAG='uhctf{why-write-code-if-we-can-use-someone-else-s-a65722}'
RUN echo ${USER_FLAG} > /home/${USERNAME}/flag.txt

# run website
EXPOSE 80
ENV USERNAME=${USERNAME}
CMD python3 /home/${USERNAME}/f2_website/app.py