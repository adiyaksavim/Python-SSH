import mysql.connector
from mysql.connector import Error
import time
import paramiko
from paramiko import BadHostKeyException, AuthenticationException, SSHException
import os 
import platform
import sys

# Mysql Connect
db = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "", 
    database = "project_py"
)
cr = db.cursor()



# SSH Login
def ssh_login():
       if os.name == 'nt':
            os.system("cls")
       else:
            os.system("clear")
       print("\n=> Centos SSH Login")
       global host_ssh, username_ssh, password_ssh
       host_ssh = input("Host/IP: ")
       username_ssh = input("Username: ")
       password_ssh = input("Password: ")
       ssh_menu()

# SSH Menu
def ssh_menu():
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
        try:
                p = paramiko.SSHClient()
                p.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
                connect = p.connect(host_ssh, port=22, username=username_ssh, password=password_ssh)
                menu_ssh = input("\nCentos SSH Menu: \n[a].Start Nginx\n[b].Stop Nginx\n[c].Cek Spec\n[d].Command\nPilih Menu: ")
                if menu_ssh == "c":
                    # sudo yum install lshw
                     if os.name == 'nt':
                                os.system("cls")
                     else:
                                os.system("clear")
                     stdin, stdout, stderr = p.exec_command("sudo yum install lshw")
                     opt = stdout.readlines()
                     opt = "".join(opt)
                     print(opt)
                     stdin, stdout, stderr = p.exec_command("sudo lshw")
                     opt = stdout.readlines()
                     opt = "".join(opt)
                     print(opt)
                     ulang_ssh_1 = input("Kembali Ke Menu Tekan y: ")
                     if ulang_ssh_1 == "y":
                        ssh_menu()
                     else:
                        sys.exit()
                elif menu_ssh == "a":
                     if os.name == 'nt':
                            os.system("cls")
                     else:
                            os.system("clear")
                     stdin, stdout, stderr = p.exec_command("systemctl start nginx")
                     opt = stdout.readlines()
                     opt = "".join(opt)
                     print(opt)
                     ulang_ssh_1 = input("Kembali Ke Menu Tekan y: ")
                     if ulang_ssh_1 == "y":
                        ssh_menu()
                     else:
                        sys.exit()
                elif menu_ssh == "b":
                     if os.name == 'nt':
                            os.system("cls")
                     else:
                            os.system("clear")
                     stdin, stdout, stderr = p.exec_command("systemctl stop nginx")
                     opt = stdout.readlines()
                     opt = "".join(opt)
                     print(opt)
                     ulang_ssh_1 = input("Kembali Ke Menu Tekan y: ")
                     if ulang_ssh_1 == "y":
                        ssh_menu()
                     else:
                        sys.exit()
                elif menu_ssh == "d":
                   def ssh_cmd():
                        if os.name == 'nt':
                                os.system("cls")
                        else:
                                os.system("clear")
                        cmd = input("\nMasukan Command: ")
                        stdin, stdout, stderr = p.exec_command(cmd)
                        opt = stdout.readlines()
                        opt = "".join(opt)
                        print(opt)
                        lanjut_cmd = input("Keluar Pencet Ctrl-c\nLanjut Cmd Tekan Sembarang: ")
                        ssh_cmd()
                   ssh_cmd()
                       

                else: 
                    ssh_menu()
        except (BadHostKeyException, AuthenticationException, 
                SSHException) as e:
                print("\nTerjadi Masalah: ", e)
                ulang_ssh = input("Coba lagi tekan y: ")
                if ulang_ssh == "y":
                    ssh_login()
                else:
                    sys.exit()
   
 
# Login System Sql
def login():
 if os.name == 'nt':
        os.system("cls")
 else:
        os.system("clear")   
 print("\n=> Login Akun")
 username = input("Masukan Username Anda: ")
 password = input("Masukan Password Anda: ")
 if username and password == "":
    print("Username Atau Password Tidak Boleh Kosong !")
    time.sleep(1)
    login()
 else:
    sql = "select * from akun where username = %s and password = %s"
    cr.execute(sql, [(username), (password)])
    hasil = cr.fetchall()
    if hasil:
        for i in hasil:
            print("Berhasil Login")
            ssh_login()
    else:
        print("Gagal Login")
        kembali_tanya = input("Ingin Register Tekan y: ")
        if kembali_tanya == "y":
          register()
        else:
          login()

# Tentang
def about():
    print("\nCentos SSH\nDeveloper: Muhammad Adiyaksa")
    time.sleep(2)
    menu_awal()

# Register
def register():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    print("\n=> Register Akun")
    username_reg = input("Daftar Username Anda: ")
    password_reg = input("Daftar Password Anda: ")
    sql_reg = "insert into akun(username, password) values('"+ username_reg +"', '"+ password_reg +"')"
    cr.execute(sql_reg)
    db.commit()
    print("Berhasil Mendaftar Akun...")
    login_ask = input("Tekan y untuk menu login: ")
    if login_ask == "y":
                login()
    else:
            menu_awal()


#  Menu Awal
def menu_awal():  
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    print("\n=> Kamu Menggunakan Operasi System:",platform.system())
    pilihan = input("CentOS SSH Python\n[a].Login\n[b].Register\n[c].Tentang Project\nPilih Menu: ")
    if pilihan == "":
        menu_awal()
    elif pilihan == "a":
        login()
    elif pilihan == "b":
        register()
    elif pilihan == "c":
        about()
    else:
        menu_awal()

menu_awal()