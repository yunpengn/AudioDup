# AudioDup - Near-duplicate Detection of Audios

This repository presents my trivial approach for near-duplicate detection of audios, by generating acoustic fingerprints.

## Setup Instructions

- We assume that you have access to a computer with MacOS. However, you should generally be fine with any Unix/Linux-based systems as well.
- Make sure you have installed [Python](https://www.python.org) 3.7 and the latest version of [pipenv](https://github.com/pypa/pipenv).
- Install MySQL connector using `brew install mysql-connector-c`.
    - Fix a potential bug by [this](https://stackoverflow.com/questions/51578425/mysqlclient-instal-error-raise-exceptionwrong-mysql-configuration-maybe-htt).
- Install `brew install portaudio && brew install ffmpeg`.
- Install all dependencies with `pipenv install`.
- Setup a databset & user for the program:

```sql
CREATE DATABASE dejavu;
CREATE USER 'dejavu'@'localhost' IDENTIFIED BY 'dejavu';
GRANT ALL PRIVILEGES ON dejavu.* TO 'dejavu'@'localhost';
```

## To Run the Program

- Collect fingerprints by `pipenv shell python3 collect.py`.
- Recognize sound from microphone by `pipenv shell python3 recognize.py`.

## Testing

- We would use the [FMA Dataset](https://github.com/mdeff/fma) to perform testing. To avoid wasting too much time & disk space, you do not have to download the whole dataset.
- Put what you downloaded into the `data` folder.
- Run `pipenv shell python3 collect.py` to collect all fingerprints.
- Run `pipenv shell python3 test.py` to collect test results.

## Licence

[GNU General Public Licence 3.0](LICENSE)
