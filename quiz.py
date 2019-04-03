from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

'''Oh no! The code is going over the edge! What are you going to do?'''
message = b'gAAAAABco998-PwCqnqduE_pmLw5nxR5ePW7npi1_fdUbQB5nC2jXWn' \
          b'_uL1GVrAJbekblmGjySI3y2u4GVM0R6rCbrWO1KIaK3R4dKDRD1yb4EENO' \
          b'NYuCx2lHoh9sptB_jOvxPyaFPzJtA92IzKEAf6TMm0Nw40LzYcg_ucvni-' \
          b'FwIxJ-t6hoj7l96samBd1hQTJ1ySpOH8K'


def main()->bytes:
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()

'''
solution URL:
https://engineering-application.britecore.com/e/t2e119s3t/testImplementationEngineer
formatted for PEP8
'''
