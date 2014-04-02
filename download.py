#!/usr/bin/python
import urllib
from pyunpack import Archive
import os
import shutil


def download(archive_url, download_to):
  print 'Downloading file...'
  urllib.urlretrieve (archive_url, download_to)
  print 'Saved to %s' % download_to


def unpack(archive_name, extract_dir):
  print 'Extracting %s' % archive_name
  Archive(archive_name).extractall(extract_dir)
  print 'Extracted to %s' % extract_dir


def create_dir(dir_name):
  if not os.path.exists(dir_name):
    os.makedirs(dir_name)


def remove_dir(dir_name):
  if os.path.exists(dir_name):
    shutil.rmtree(dir_name)


if __name__ == '__main__':
  archive_url='http://w1.c1.rada.gov.ua/pls/zweb2/webproc34?id=&pf3511=50433&pf35401=295756'
  local_filename = 'budget.rar'
  extract_dir = 'temp/'
  remove_dir(extract_dir)
  create_dir(extract_dir)
  download(archive_url, local_filename)
  unpack(local_filename, extract_dir)

