# crypto-bbs
Encrypted Anonymous BBS (work in progress)

This Django 1.7 project implements a flexible and easily extensible BBS with RESTful API for posting and retrieving via AJAJ calls.

To-Do:

The data sent and retrieved by this application will be encrypted and decrypted in the client browser using: https://code.google.com/p/crypto-js/

***NOTE:*** This is a good starting framework for anything else you might like to make. It is also in-progress, so fork and use at your own risk. Of special note, this application (by design) does not authenticate any users. It is strictly anonymous. This can be easily reversed, but users are not validated in the views. Again this is by design and not an accidental oversight.
