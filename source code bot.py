from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Ganti dengan token bot Anda
TOKEN = '7783061926:AAEqCLJsB9_ZD13ROZSB0Aa16YTmQWpAKGU'

# Fungsi untuk menyapa pengguna dan menampilkan menu utama
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    welcome_message = f"Selamat datang {user.first_name}! Terima kasih telah mengakses pelayanan DTEDI. Silakan pilih layanan!"
    
    # Membuat tombol untuk menu utama
    keyboard = [
        [InlineKeyboardButton("INFO DTEDI", callback_data='info_dted')],
        [InlineKeyboardButton("MBKM dan Praktik Industri", callback_data='mbkm')],
        [InlineKeyboardButton("Beasiswa", callback_data='beasiswa')],
        [InlineKeyboardButton("KKN", callback_data='kkn')],
        [InlineKeyboardButton("Program Studi DTEDI", callback_data='program_studi')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

# Fungsi untuk menangani pilihan tombol
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    choice = query.data
    await query.answer()

    # Mengatur respons berdasarkan pilihan pengguna
    if choice == 'info_dted':
        await show_info_dted(query, context)
    elif choice == 'mbkm':
        await show_mbkm_praktik(query, context)
    elif choice == 'beasiswa':
        await show_beasiswa(query, context)
    elif choice == 'kkn':
        await show_kkn(query, context)
    elif choice == 'program_studi':
        await show_program_studi_menu(query, context)
    elif choice == 'main_menu':
        await start(query, context)
    else:
        await info_responses(query, choice)

# Fungsi untuk menampilkan submenu INFO DTEDI
async def show_info_dted(query, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Kontak Akademik DTEDI", callback_data='kontak_akademik')],
        [InlineKeyboardButton("Kurikulum DTEDI", callback_data='kurikulum')],
        [InlineKeyboardButton("Kalender Akademik UGM", callback_data='kalender_akademik')],
        [InlineKeyboardButton("Kembali ke Menu Utama", callback_data='main_menu')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Silakan pilih layanan INFO DTEDI:", reply_markup=reply_markup)

# Fungsi untuk menampilkan submenu MBKM dan Praktik Industri
async def show_mbkm_praktik(query, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Program MBKM", callback_data='program_mbkm')],
        [InlineKeyboardButton("Praktik Industri", callback_data='praktik_industri')],
        [InlineKeyboardButton("Kembali ke Menu Utama", callback_data='main_menu')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Silakan pilih layanan MBKM dan Praktik Industri:", reply_markup=reply_markup)

# Fungsi untuk menampilkan submenu Beasiswa
async def show_beasiswa(query, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Info Beasiswa", callback_data='info_beasiswa')],
        [InlineKeyboardButton("Kembali ke Menu Utama", callback_data='main_menu')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Silakan pilih layanan Beasiswa:", reply_markup=reply_markup)

# Fungsi untuk menampilkan submenu KKN
async def show_kkn(query, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Info KKN", callback_data='info_kkn')],
        [InlineKeyboardButton("Kembali ke Menu Utama", callback_data='main_menu')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Silakan pilih layanan KKN:", reply_markup=reply_markup)

# Fungsi untuk menampilkan submenu Program Studi DTEDI
async def show_program_studi_menu(query, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Teknologi Rekayasa Internet", callback_data='tri')],
        [InlineKeyboardButton("Teknologi Rekayasa Elektro", callback_data='tre')],
        [InlineKeyboardButton("Teknologi Rekayasa Perangkat Lunak", callback_data='trpl')],
        [InlineKeyboardButton("Teknologi Rekayasa Instrumentasi & Kontrol", callback_data='trik')],
        [InlineKeyboardButton("Kembali ke Menu Utama", callback_data='main_menu')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Silakan pilih Program Studi DTEDI:", reply_markup=reply_markup)

# Fungsi untuk menangani tombol akhir di INFO DTEDI dan submenu lainnya
async def info_responses(query, choice):
    info_texts = {
        'kontak_akademik': (
    "Alamat Surel Akademik DTEDI: tedi.sv@ugm.ac.id\n"
    "Nomor Whatsapp Akademik DTEDI: 08157999995\n"
    "Fax: (0274) 542908\n"
    "Telepon: (0274) 6491302, 561111\n"
    "Situs web: tedi.sv.ugm.ac.id\n"
    "Instagram: @dtedi.sv.ugm\n"),

        'kurikulum': ("Berikut tautan untuk mengakses kurikulum pada Departemen Teknik Elektro dan Informatika:\n"
    "https://tedi.sv.ugm.ac.id/wp-content/uploads/sites/26/2019/10/Kurikulum-TEDI-2019.pdf"),

        'kalender_akademik': ("Berikut tautan untuk mengakses kalender akademik Departemen Teknik Elektro dan Informatika:\n"
    "https://tedi.sv.ugm.ac.id/id/kalender-akademik/"),

        'program_mbkm': ("Alur MBKM DTEDI:\n"
    "https://docs.google.com/viewerng/viewer?url=https://trpl.sv.ugm.ac.id/wp-content/uploads/sites/1382/2024/08/Alur-MBKM-DTEDI-2023-v2.0-Mei-2023-1.pdf&hl=en\n"
    "Permohonan Surat Rekomendasi MBKM 2024 (Merdeka Belajar Kampus Merdeka):\n"
    "https://docs.google.com/forms/d/e/1FAIpQLSeaS6P-q0BnPx8o91-DmDC1XvhzyWLVU6G9XPIWjd4sCjuYvA/viewform\n"
    "Pendaftaran: https://kampusmerdeka.kemdikbud.go.id/"),

        'praktik_industri': (
    "Berikut tautan untuk mengakses alur praktik industri dan alur seminar praktik industri:\nhttps://tri.sv.ugm.ac.id/praktik-industri/"),

        'info_beasiswa': ("Informasi Beasiswa:\n"
    "1. https://ditmawa.ugm.ac.id/category/info-beasiswa/\n"
    "2. https://simaster.ugm.ac.id/kemahasiswaan/beasiswa/"),

        'info_kkn': ( "Persyaratan Administrasi Peserta KKN:\n"
    "1. Dikirimkan/diverifikasi sebagai peserta KKN-PPM oleh Admin Fakultas.\n"
    "2. Mahasiswa calon peserta KKN-PPM wajib mengikuti pembekalan KKN-PPM sesuai dengan jadwal yang ditentukan.\n"
    "3. Mahasiswa melakukan pembayaran biaya KKN-PPM melalui Bank BNI dan pemeriksaan kesehatan di GMC Health Center sesuai dengan jadwal yang telah ditentukan.\n"
    "4. Verifikasi persyaratan akademik dan administratif calon peserta KKN-PPM dilakukan oleh fakultas (akademik) dengan memberikan username dan password sebagai tanda kelayakan sebagai peserta KKN-PPM. "
    "Bagi calon peserta yang memenuhi ketentuan (lulus pembekalan, membayar biaya KKN-PPM, sehat, memenuhi syarat jumlah SKS dan tidak dalam kondisi hamil bagi mahasiswi) akan memperoleh password – username dan selanjutnya melakukan input data (log in) secara mandiri.\n"
    "5. Peserta KKN-PPM adalah calon peserta yang telah berhasil melakukan input data (log in) melalui website www.kkn.ugm.ac.id.\n\n"
    
    "Persyaratan Akademik Peserta KKN PPM:\n"
    "1. Terdaftar sebagai mahasiswa aktif.\n"
    "2. Kegiatan Wajib Bagi Mahasiswa Universitas Gadjah Mada dengan bobot 3 SKS yang dilaksanakan oleh mahasiswa yang telah menempuh kuliah dan praktikum minimum 100 SKS dan dilakukan dalam waktu minimum 2 bulan atau setara dengan 360 jam kerja efektif untuk setiap mahasiswa tanpa ada nilai E "
    "(Sesuai Surat Keputusan Rektor Universitas Gadjah Mada Nomor 245/P/SK/HT/2008 tentang Perubahan Keputusan Rektor Universitas Gadjah Mada No 283/P/SK/HT/2006 tentang Kuliah Kerja Nyata-Pembelajaran Pemberdayaan Masyarakat Universitas Gadjah Mada).\n"
    "3. Terdaftar sebagai peserta KKN-PPM di fakultas yang dibuktikan dengan KRS pada semester saat KKN-PPM dilakukan.\n"
    "4. Tidak sedang mengambil mata kuliah dan praktikum.\n"
    "5. Memasukkan Mata Kuliah KKN-PPM pada KRS Semester Genap bagi peserta KKN-PPM.\n"
    "6. Semester Genap, dan bagi Peserta KKN-PPM Antar Semester memasukkan mata kuliah KKN-PPM pada KRS sesuai dengan ketentuan/kebijakan fakultas masing-masing.\n"
    "7. Pengiriman daftar calon peserta KKN-PPM dari fakultas ke LPPM berdasarkan usulan matakuliah dalam KRS mahasiswa sesuai jadwal."),

        'tri': (
    "https://tri.sv.ugm.ac.id/\n\n"

    "Program Studi\n"
    "Program Studi Sarjana Terapan (D-IV) Teknologi Rekayasa Internet di Sekolah Vokasi UGM didirikan pada 2013 untuk memenuhi kebutuhan industri dan pemerintah di bidang TI. "
    "Program ini berfokus pada teknologi jaringan, sistem informasi, keamanan jaringan, dan pengembangan aplikasi internet, serta melatih keterampilan praktis dalam infrastruktur jaringan, komputasi awan, virtualisasi, manajemen server, dan keamanan siber.\n\n"
    
    "Profil Lulusan\n"
    "1. Network Engineer: Menguasai konsep jaringan, mampu merancang, mengonfigurasi, dan membangun infrastruktur jaringan; memahami telekomunikasi dan teknologi nirkabel.\n"
    "2. Cyber Security Engineer: Menguasai keamanan siber pada jaringan, aplikasi, dan data; mampu merancang aplikasi dan infrastruktur keamanan.\n"
    "3. IoT Engineer: Menguasai dan merekayasa perangkat IoT.\n"
    "4. Cloud Computing Engineer: Menguasai komputasi awan, auto-scaling, dan multi-cluster; mampu merancang infrastruktur awan.\n"
    "5. Technopreneur: Menguasai technopreneurship; merancang strategi dan mengelola bisnis TI.\n\n"
    
    "Kompetensi\n"
    "Kompetensi mahasiswa dibuktikan dengan program sertifikasi profesional dari vendor perangkat teknologi, antara lain:\n"
    "- Mikrotik Academy\n"
    "- Ec-Council Academy\n"
    "- Huawei Academy\n"
    "- Netacad (Cisco Academy)\n"
    "- Alibaba Cloud Academy\n\n"
    
    "Akreditasi: Akreditasi Baik (B)\n\n"
    
    "Fasilitas\n"
    "- Laboratorium Layanan Internet\n"
    "- Laboratorium Jaringan Komputer\n"
    "- Laboratorium Perangkat Lunak (Software)\n"
    "- Laboratorium Perangkat Keras (Hardware)\n"
    "- Portal E-Learning\n"
    "- Ruang Karya\n"
    "- Ruang Proyek Akhir\n"
    "- Ruang Server\n"
    "- Gazebo\n"
    "- Musholla\n"
    "- CCTV\n"
    "- Free WiFi Area\n"
    "- Parkir\n"),

        'tre': (
    "https://tre.sv.ugm.ac.id/\n\n"

    "Program Studi\n"
    "Program Studi (Prodi) Teknologi Rekayasa Elektro (TRE) fokus pada teknologi kelistrikan, dari pembangkitan hingga pemanfaatan energi secara efisien.\n"
    "Mahasiswa mempelajari rangkaian listrik, sistem tenaga, teknik pengukuran, dan kontrol sistem tenaga.\n"
    "Prodi ini mengembangkan keterampilan pemasangan, uji coba, troubleshooting, dan perawatan sistem kelistrikan.\n"
    "Lulusan diharapkan siap bekerja sebagai teknisi, perancang sistem tenaga, atau konsultan energi, serta menghadapi tantangan efisiensi energi dan integrasi smart grid.\n\n"
    
    "Profil Lulusan\n"
    "1. Ahli Teknik Listrik: Mampu merancang dan memelihara sistem kelistrikan untuk berbagai skala.\n"
    "2. Teknisi Sistem Tenaga Listrik: Siap dalam instalasi dan perawatan sistem tenaga listrik serta menangani masalah teknis.\n"
    "3. Perancang Sistem Energi Terbarukan: Mampu merancang sistem energi terbarukan seperti tenaga surya dan angin.\n"
    "4. Konsultan Energi: Menawarkan solusi efisiensi energi dan meningkatkan kinerja sistem kelistrikan.\n"
    "5. Engineer Sistem Otomasi: Mengembangkan sistem otomatisasi kelistrikan dengan teknologi PLC dan SCADA.\n"
    "6. Peneliti Teknologi Kelistrikan: Berkontribusi dalam penelitian dan pengembangan teknologi listrik dan smart grid.\n"
    "7. Manajer Proyek Energi: Memimpin proyek kelistrikan dari perencanaan hingga pengawasan.\n"
    "8. Entrepreneur Teknologi Kelistrikan: Mampu memulai usaha di bidang sistem tenaga listrik dan energi terbarukan.\n\n"
    
    "Akreditasi: Akreditasi Baik (B)\n\n"
    
    "Fasilitas\n"
    "Laboratorium:\n"
    "- Laboratorium Layanan Listrik Dasar\n"
    "- Laboratorium Instalasi Listrik\n"
    "- Laboratorium Mesin-Mesin Listrik\n"
    "- Laboratorium Proteksi dan Distribusi\n"
    
    "Fasilitas Lainnya:\n"
    "Portal E-Learning, Ruang Karya, Ruang Proyek Akhir, Ruang Server, Gazebo, Musholla, CCTV, Free WiFi, dan Area Parkir.\n"),

        'trpl': (
    "https://trpl.sv.ugm.ac.id/\n\n"

    "Program Studi\n"
    "Program Studi Sarjana Terapan Teknologi Rekayasa Perangkat Lunak memfokuskan pada pengembangan perangkat lunak berorientasi industri. "
    "Mahasiswa dibekali keterampilan analisis sistem, pengembangan perangkat lunak, pengelolaan basis data, serta pembuatan game dan multimedia. "
    "Lulusan memiliki peluang karir sebagai Analis Sistem, Perekayasa Perangkat Lunak, Administrator Basis Data, dan Pengembang Game, siap menghadapi tantangan industri teknologi.\n\n"

    "Profil Lulusan\n"
    "1. System Analyst: Mampu menganalisis dan merancang perangkat lunak sesuai kebutuhan.\n"
    "2. Perekayasa Perangkat Lunak: Mampu mengembangkan (Programmer), menguji dan memvalidasi (Quality Assurance) perangkat lunak.\n"
    "3. Administrator Basis Data: Mampu mendesain, mengimplementasikan, dan mengelola basis data.\n"
    "4. Pengembang Game dan Multimedia: Mampu mengembangkan produk game dan multimedia.\n\n"

    "Akreditasi: Akreditasi Baik (B)\n\n"

    "Fasilitas\n"
    "- Gedung sendiri untuk pelaksanaan proses belajar mengajar.\n"
    "- 12 ruang kelas, masing-masing berkapasitas 60 orang.\n"
    "- 12 laboratorium: 9 ruang komputer, 1 studio multimedia, 1 ruang SI, dan 1 ruang Technopreneurship.\n"
    "- Setiap ruang laboratorium dilengkapi dengan 25 komputer (dual-core hingga core i5), AC, proyektor, dan whiteboard.\n"
    "- Studio multimedia dilengkapi dengan komputer core i5 hingga core i7 dan peralatan animasi.\n"
    "- 6 ruang dosen dan 3 ruang administrasi, masing-masing dilengkapi dengan AC.\n"
    "- Ruangan terbuka bagi mahasiswa seluas 50 meter persegi.\n"
    "- Mushola seluas 100 meter persegi.\n"
    "- Area parkir untuk 400 kendaraan roda dua dan 30 kendaraan roda empat.\n"
    "- 3 toilet dengan luas masing-masing 50 meter persegi.\n"
    "- Internet 20 Mbps yang mencakup seluruh gedung berlantai dua.\n"),

        'trik': (
    "https://trik.sv.ugm.ac.id/"
    "Program Studi\n"
    "Program studi Teknologi Rekayasa Instrumentasi dan Kontrol (TRIK) mempersiapkan Anda untuk menjadi ahli di bidang Instrumentasi dan Kontrol. "
    "Dapatkan kompetensi dalam perancangan, pengoperasian, dan perbaikan sistem Instrumentasi, Metrologi, Kontrol, Otomasi, dan Robotika di industri.\n\n"
    
    "Akreditasi: Akreditasi Baik (B)\n\n"

    "Keunggulan\n"
    "1. Prospek Karier Luas: Peluang kerja di BUMN seperti Pertamina, PLN, PGN, dan Indonesia Power; juga di perusahaan internasional seperti Siemens, ABB, dan Schneider.\n"
    "2. Kesempatan di Perusahaan Swasta: Peluang di sektor Instrumentasi dan Kontrol di perusahaan swasta nasional.\n"
    "3. Karir di Lembaga Penelitian: Kesempatan berkarir di lembaga penelitian seperti BPPT, LIPI, dan BATAN.\n"
    "4. Dosen Berkualitas: Dosen kompeten dengan sertifikasi keahlian industri.\n"
    "5. Sarana dan Prasarana Lengkap: Tersedia laboratorium dan fasilitas modern untuk pembelajaran.\n"
    "6. Kurikulum Mendukung Sertifikasi: Kurikulum dirancang untuk mendukung sertifikasi sebagai Instrument Engineer, Control Engineer, dan SCADA Engineer.\n"
    "7. Kerjasama dengan Perusahaan Terkenal: Kolaborasi dengan perusahaan terkemuka untuk pengembangan karier dan kualitas pendidikan.\n"
    "8. Kesempatan Internasional: Program pertukaran mahasiswa dan kerjasama internasional tersedia.\n\n"
    
    "Pilih Program Studi TRIK untuk membangun karier yang menjanjikan di Instrumentasi dan Kontrol.\n\n"
    
    "Organisasi\n"
    "HIMATRIK (Himpunan Mahasiswa Teknologi Rekayasa Instrumentasi dan Kontrol)\n"
    "Instagram : @himatrik.ugm\n\n"
    
    "Kontak\n"
    "Telp. (0274) 6491302, 561111\n"
    "Email : trik.sv@ugm.ac.id\n"
    "Fax. (0274) 542908\n"),
    }
    
    if choice in info_texts:
        # Menambahkan tombol "Kembali ke Menu Utama"
        keyboard = [[InlineKeyboardButton("Kembali ke Menu Utama", callback_data='main_menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Menampilkan informasi pilihan dengan tombol "Kembali ke Menu Utama"
        await query.edit_message_text(text=info_texts[choice], reply_markup=reply_markup)

# Fungsi untuk menangani semua tombol akhir di dalam submenus
async def handle_final_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    choice = query.data
    await query.answer()
    
    # Menangani respon akhir
    await info_responses(query, choice)

# Fungsi utama untuk menjalankan bot
def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Menambahkan handler
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))
    
    # Menambahkan handler untuk tombol akhir
    for btn in ['kontak_akademik', 'kurikulum', 'kalender_akademik', 
                'program_mbkm', 'praktik_industri', 'info_beasiswa', 'info_kkn', 
                'tri', 'tre', 'trpl', 'trik']:
        application.add_handler(CallbackQueryHandler(handle_final_buttons, pattern=btn))

    # Menjalankan bot
    application.run_polling(timeout=30)

if __name__ == '__main__':
    main()
