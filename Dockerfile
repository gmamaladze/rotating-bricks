FROM ubuntu:16.04

RUN apt-get update && \
	  apt-get install -y curl bzip2 libfreetype6 libgl1-mesa-dev libglu1-mesa libxi6 libxrender1 && \
	  apt-get -y autoremove && \
	  rm -rf /var/lib/apt/lists/*

ENV BLENDER_MAJOR 2.78
ENV BLENDER_VERSION 2.78a
ENV BLENDER_BZ2_URL http://download.blender.org/release/Blender$BLENDER_MAJOR/blender-$BLENDER_VERSION-linux-glibc211-x86_64.tar.bz2

RUN curl -Ls ${BLENDER_BZ2_URL} | tar -xjv -C /opt && \
    ln -s /opt/blender-${BLENDER_VERSION}-linux-glibc211-x86_64 /opt/blender

ENV PATH=/opt/blender:$PATH

ADD brick.obj /brick.obj

ADD main.py /main.py

CMD ["blender", "--background", "--python", "/main.py"]
