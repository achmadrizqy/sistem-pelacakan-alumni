from flask import Flask, render_template, request, redirect
import random
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS alumni (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        tahun TEXT,
        prodi TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS hasil_pelacakan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        pekerjaan TEXT,
        instansi TEXT,
        confidence REAL,
        status TEXT,
        sumber TEXT,
        jabatan TEXT,
        lokasi TEXT,
        bidang_publikasi TEXT,
        tahun_aktivitas TEXT,
        link_profil TEXT,
        ringkasan_informasi TEXT,
        link_bukti TEXT
    )
    """)

    # Pastikan schema terbaru (jika sudah ada database lama, tambahkan kolom baru)
    for column, col_def in [
        ("jabatan", "TEXT"),
        ("lokasi", "TEXT"),
        ("bidang_publikasi", "TEXT"),
        ("tahun_aktivitas", "TEXT"),
        ("link_profil", "TEXT"),
        ("ringkasan_informasi", "TEXT"),
        ("link_bukti", "TEXT")
    ]:
        try:
            cur.execute(f"ALTER TABLE hasil_pelacakan ADD COLUMN {column} {col_def}")
        except Exception:
            # Kolom sudah ada atau tidak bisa ditambahkan
            pass

    conn.commit()
    conn.close()

# ===============================
# DATA SEMENTARA (SIMULASI DATABASE)
# ===============================

data_alumni = [
    {"nama": "rizqy", "tahun": "2021", "prodi": "informatika"},
    {"nama": "supaidi", "tahun": "2019", "prodi": "informatika"}
]

hasil_pelacakan = []


# ===============================
# DASHBOARD
# ===============================

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db()
    cur = conn.cursor()

    # Tambah alumni
    if request.method == "POST" and "tambah_alumni" in request.form:
        nama = request.form["nama"]
        tahun = request.form["tahun"]
        prodi = request.form["prodi"]
        cur.execute(
            "INSERT INTO alumni (nama,tahun,prodi) VALUES (?,?,?)",
            (nama, tahun, prodi)
        )
        conn.commit()

    # Hapus alumni
    if request.method == "POST" and "hapus_alumni" in request.form:
        alumni_id = request.form["alumni_id"]
        cur.execute("DELETE FROM alumni WHERE id=?", (alumni_id,))
        conn.commit()

    # Jalankan pelacakan
    if request.method == "POST" and "jalankan_pelacakan" in request.form:
        pekerjaan_list = [
            "Software Engineer",
            "Data Analyst",
            "Researcher",
            "System Administrator"
        ]
        instansi_list = [
            "Startup Teknologi",
            "Perusahaan IT",
            "Universitas",
            "Perusahaan Swasta"
        ]
        sumber_list = [
            "Google",
            "LinkedIn",
            "Instagram",
            "Scholar",
            "ORCID",
            "ResearchGate",
            "GitHub",
            "Kaggle",
            "Directory Perusahaan",
            "Press Release",
            "Publikasi Akademik",
            "Web Umum"
        ]
        cur.execute("SELECT * FROM alumni")
        alumni = cur.fetchall()
        # Kosongkan hasil sebelumnya
        cur.execute("DELETE FROM hasil_pelacakan")
        for a in alumni:
            # Variasi nama
            nama_variasi = [a["nama"], a["nama"].split()[0] if len(a["nama"].split()) > 1 else a["nama"]]
            # Kata kunci afiliasi
            afiliasi = ["Universitas Muhammadiyah Malang", "UMM", a["prodi"]]
            # Kata kunci konteks
            konteks = [a["prodi"], a["tahun"], "Malang"]
            
            # Simulasi ekstraksi informasi kandidat
            jabatan = random.choice(["Software Engineer", "Data Analyst", "Researcher", "System Administrator", "Lecturer"])
            lokasi = random.choice(["Malang", "Jakarta", "Surabaya", "Bandung"])
            bidang_publikasi = random.choice(["Computer Science", "Data Science", "AI", "Software Development"])
            tahun_aktivitas = str(random.randint(int(a["tahun"]), 2026))
            link_profil = f"https://linkedin.com/in/{a['nama'].lower().replace(' ', '')}"
            
            # Ringkasan informasi dan link bukti
            ringkasan_informasi = f"Alumni {a['nama']} ditemukan sebagai {jabatan} di {lokasi}, bidang {bidang_publikasi}."
            link_bukti = f"https://scholar.google.com/citations?user={a['nama'].lower().replace(' ', '')}"
            
            pekerjaan = random.choice(pekerjaan_list)
            instansi = random.choice(instansi_list)
            sumber = random.choice(sumber_list)
            skor = round(random.uniform(0,1),2)
            if skor > 0.8:
                status = "Teridentifikasi"
            elif skor > 0.5:
                status = "Perlu Verifikasi"
            else:
                status = "Belum Ditemukan"
            cur.execute(
                """
                INSERT INTO hasil_pelacakan 
                (nama, pekerjaan, instansi, confidence, status, sumber, jabatan, lokasi, bidang_publikasi, tahun_aktivitas, link_profil, ringkasan_informasi, link_bukti)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (a["nama"], pekerjaan, instansi, skor, status, sumber, jabatan, lokasi, bidang_publikasi, tahun_aktivitas, link_profil, ringkasan_informasi, link_bukti)
            )
        conn.commit()

    # Reset hasil pelacakan
    if request.method == "POST" and "reset_hasil" in request.form:
        cur.execute("DELETE FROM hasil_pelacakan")
        conn.commit()

    # Ambil data alumni dan hasil pelacakan
    cur.execute("SELECT * FROM alumni")
    alumni = cur.fetchall()
    cur.execute("SELECT * FROM hasil_pelacakan")
    hasil = cur.fetchall()
    conn.close()
    return render_template("index.html", alumni=alumni, hasil=hasil)






# ===============================
# MENJALANKAN SERVER
# ===============================

if __name__ == "__main__":
    init_db()
    # Render passes the port in the PORT environment variable.
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)