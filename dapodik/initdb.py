import pymysql

host = 'localhost'
user = 'pedro'
password = '1'
dbname = 'python'

def get_cursor(db):
    return db.cursor()

def create_db():
    db = pymysql.connect(host, user, password, dbname)
    cursor = db.cursor()
    # drop_provinsi = """DROP TABLE IF EXISTS Provinsi"""
    drop_kabupaten = """DROP TABEL IF EXISTS Kabupaten"""
    # create_provinsi = """CREATE TABLE Provinsi (
    #     provinsiid int, nama_provinsi varchar(50), total_sekolah float, total_kirim float, total_sisa float, total_sd float, total_kirim_sd float,
    #     total_sisa_sd float, total_smp float, total_kirim_smp float, total_sisa_smp float, total_sma float, total_kirim_sma float, total_sisa_sma float,
    #     total_slb float, total_kirim_slb float, total_sisa_slb float, total_smk float, total_kirim_smk float,
    #     total_sisa_smk float, PRIMARY KEY (provinsiid) );"""
    create_kabupaten = """CREATE TABLE Kabupaten (
        kabupatenid int, provinsiid int, nama_kabupaten varchar(50), total_sekolah float, total_kirim float, total_sisa float, total_sd float, total_kirim_sd float,
        total_sisa_sd float, total_smp float, total_kirim_smp float, total_sisa_smp float, total_sma float, total_kirim_sma float, total_sisa_sma float,
        total_slb float, total_kirim_slb float, total_sisa_slb float, total_smk float, total_kirim_smk float,
        total_sisa_smk float, PRIMARY KEY (kabupatenid), FOREIGN KEY (provinsiid) REFERENCES Provinsi(provinsiid) );"""
    try:
        cursor.execute(create_provinsi)
        cursor.execute(create_kabupaten)
    except:
        # cursor.execute(drop_provinsi)
        # cursor.execute(create_provinsi)
        cursor.execute(drop_kabupaten)
        cursor.execute(create_kabupaten)
    return db