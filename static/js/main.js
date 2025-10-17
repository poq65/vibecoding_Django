// 메시지 자동 숨김 기능
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.add('fade');
            setTimeout(() => alert.remove(), 500);
        }, 3000);
    });
});

// 폼 유효성 검사
function validateForm() {
    const title = document.querySelector('#id_title');
    const content = document.querySelector('#id_content');
    let isValid = true;

    if (title && !title.value.trim()) {
        isValid = false;
        title.classList.add('is-invalid');
    }

    if (content && !content.value.trim()) {
        isValid = false;
        content.classList.add('is-invalid');
    }

    return isValid;
}

// 메모 삭제 확인
function confirmDelete(event) {
    if (!confirm('정말로 이 메모를 삭제하시겠습니까?')) {
        event.preventDefault();
    }
}

// 입력 필드 문자 수 표시
document.addEventListener('DOMContentLoaded', function() {
    const titleInput = document.querySelector('#id_title');
    const contentInput = document.querySelector('#id_content');

    if (titleInput) {
        titleInput.addEventListener('input', function() {
            const remaining = 200 - this.value.length;
            const counter = document.querySelector('#title-counter');
            if (counter) {
                counter.textContent = `${remaining} 자 남음`;
            }
        });
    }

    if (contentInput) {
        contentInput.addEventListener('input', function() {
            const counter = document.querySelector('#content-counter');
            if (counter) {
                counter.textContent = `${this.value.length} 자`;
            }
        });
    }
});

// 반응형 네비게이션 바
document.addEventListener('DOMContentLoaded', function() {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');

    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', function() {
            navbarCollapse.classList.toggle('show');
        });
    }
});

// 메모 카드 애니메이션
document.addEventListener('DOMContentLoaded', function() {
    const memoCards = document.querySelectorAll('.card');
    memoCards.forEach(card => {
        card.classList.add('fade-in');
    });
});