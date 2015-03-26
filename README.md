# crypto-bbs
Encrypted Anonymous BBS ***IN-PROGRESS and EXPERIMENTAL***

This Django 1.7 project implements a key-access BBS with RESTful API (via Django REST Framework) for posting and retrieving via AJAJ calls.

To-Do:
+ Add a 'key' form field for accessing Board endpoints and encrypting/decrypting Posts
+ All data sent and retrieved by this application will be encrypted and decrypted in the client browser using: https://code.google.com/p/crypto-js/

***NOTE:*** Fork and use at your own risk. Of special note, this application (by design) does not authenticate any users. It is strictly anonymous. This can be easily reversed, but users are not validated in the views. Again this is by design and not an accidental oversight.
