
FROM debian:9.8
LABEL maintainer="mdoulaty@gmail.com"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        g++ \
        make \
        automake \
        autoconf \
        bzip2 \
        unzip \
        wget \
        sox \
        libtool \
        git \
        subversion \
        python2.7 \
        python3 \
        zlib1g-dev \
        ca-certificates \
        patch \
        ffmpeg \
	vim && \
    rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python2.7 /usr/bin/python 

RUN git clone --depth 1 https://github.com/chizhang0814/kaldi.git /opt/kaldi && \
    cd /opt/kaldi && \
    cd /opt/kaldi/tools && \
    ./extras/install_mkl.sh && \
    apt-get -y install gfortran && \
    make -j $(nproc) && \
    cd /opt/kaldi/src && \
    ./configure --shared && \
    make depend -j $(nproc) && \
    make -j $(nproc)&& \ 
    export PATH=$PATH:/opt/kaldi/tools/openfst:/opt/kaldi/src/featbin:/opt/kaldi/src/gmmbin:/opt/kaldi/src/bin:/opt/kaldi/src/latbin:/opt/kaldi/src/nnetbin:/opt/kaldi/src/nnet2bin:/opt/kaldi/src/nnet3bin:/opt/kaldi/tools/srilm/bin:/opt/kaldi/tools/srilm/bin/i686-m64:/opt/kaldi/tools/irstlm/bin && \
    git clone --depth 1 https://github.com/chizhang0814/gst-kaldi-nnet2-online.git /opt/gst-kaldi-nnet2-online && \
    apt-get -y install gstreamer1.0-plugins-bad  gstreamer1.0-plugins-base gstreamer1.0-plugins-good  gstreamer1.0-pulseaudio  gstreamer1.0-plugins-ugly  gstreamer1.0-tools libgstreamer1.0-dev && \
    apt-get -y install libjansson-dev && \
    cd /opt/gst-kaldi-nnet2-online/src && \
    KALDI_ROOT=/opt/kaldi make depend && \
    KALDI_ROOT=/opt/kaldi mak && \
    export GST_PLUGIN_PATH=/opt/gst-kaldi-nnet2-online/src

WORKDIR /opt/kaldi/

