document.addEventListener('DOMContentLoaded', function() {
    // 移动端菜单交互
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileMenu = document.querySelector('.mobile-menu');
    
    if (mobileMenuBtn && mobileMenu) {
      mobileMenuBtn.addEventListener('click', function() {
        mobileMenu.classList.toggle('active');
        
        // 切换图标
        const icon = mobileMenuBtn.querySelector('i');
        if (icon.classList.contains('fa-bars')) {
          icon.classList.remove('fa-bars');
          icon.classList.add('fa-times');
        } else {
          icon.classList.remove('fa-times');
          icon.classList.add('fa-bars');
        }
      });
    }
    
    // 设置copyright年份
    const currentYear = new Date().getFullYear();
    const copyrightYear = document.querySelector('.copyright span');
    if (copyrightYear) {
      copyrightYear.textContent = currentYear;
    }
    
    // 关闭flash消息
    const closeFlashButtons = document.querySelectorAll('.close-flash');
    if (closeFlashButtons.length > 0) {
      closeFlashButtons.forEach(button => {
        button.addEventListener('click', function() {
          const flashMessage = this.closest('.flash-message');
          if (flashMessage) {
            flashMessage.style.display = 'none';
          }
        });
      });
      
      // 5秒后自动关闭flash消息
      setTimeout(function() {
        document.querySelectorAll('.flash-message').forEach(message => {
          message.style.display = 'none';
        });
      }, 5000);
    }
  });