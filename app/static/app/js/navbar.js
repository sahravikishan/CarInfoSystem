// Navbar Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.querySelector('.navbar-toggle');
    const menu = document.querySelector('.navbar-menu');
    
    if (toggle && menu) {
        toggle.addEventListener('click', function() {
            if (menu.style.display === 'none' || menu.style.display === '') {
                menu.style.display = 'flex';
                menu.style.flexDirection = 'column';
                menu.style.position = 'absolute';
                menu.style.top = '70px';
                menu.style.left = '0';
                menu.style.right = '0';
                menu.style.backgroundColor = '#0F1C2E';
                menu.style.padding = '16px 24px';
                menu.style.borderBottom = '1px solid rgba(212, 165, 116, 0.2)';
                menu.style.gap = '12px';
            } else {
                menu.style.display = 'none';
            }
        });
        
        // Close menu when clicking on a link
        menu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function() {
                menu.style.display = 'none';
            });
        });
    }
});
