FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# python
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

WORKDIR /workspaces/bioinformatics-training

COPY requirements.txt .

# install python packages
RUN pip install -r requirements.txt

# install bioinformatics apt packages
RUN apt-get install -y fastqc scythe sickle bowtie2 samtools bcftools

# install general apt packages
RUN apt-get install -y curl less vim


ENTRYPOINT ["python3"]