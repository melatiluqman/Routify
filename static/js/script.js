function toggleDropdown() {
    const dropdown = document.getElementById('dropdown-menu');
    dropdown.classList.toggle('active'); // Tambahkan atau hapus class 'active'
}

// Tutup dropdown ketika klik di luar area dropdown
document.addEventListener('click', function (event) {
    const dropdown = document.getElementById('dropdown-menu');
    const profileIcon = document.querySelector('.profile-icon');
    if (!profileIcon.contains(event.target) && !dropdown.contains(event.target)) {
        dropdown.classList.remove('active'); // Hapus class 'active' jika klik di luar
    }
});

