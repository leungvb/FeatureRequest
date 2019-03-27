from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcm7AR-HTMsCg2AzVDI3dI2y7pnNpNS-JSOCR2vtbxz2Z3EQyX8jJPO6ja-Z1SyORwQHfCnwe051la88Y136iW7pgZfYBT1O_AhfRbMzb_1GCl-hhUIs7CeDFcOxbOWNisMg5K2opvMVPcXjhl3bCwr6nPID5EegydXUIn_rqJnLANZ5u64Sl8J47qe97drzh6yr_x'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()