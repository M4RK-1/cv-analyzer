function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    if (sidebar.style.width === '60px') {
        sidebar.style.width = '220px';
        document.querySelectorAll('.sidebar a').forEach(el => el.style.display = 'block');
    } else {
        sidebar.style.width = '60px';
        document.querySelectorAll('.sidebar a').forEach(el => el.style.display = 'none');
    }
}
