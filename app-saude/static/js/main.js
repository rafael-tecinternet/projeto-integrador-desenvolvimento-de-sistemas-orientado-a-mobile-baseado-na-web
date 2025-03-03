document.addEventListener('DOMContentLoaded', function() {
    // Login via AJAX (se utilizado no login.html)
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            fetch('/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    document.getElementById('login-message').innerText = data.message;
                    window.location.href = '/dashboard';
                } else {
                    document.getElementById('login-message').innerText = data.error || 'Erro no login.';
                }
            })
            .catch(error => console.error('Erro:', error));
        });
    }

    // Registro via AJAX (se utilizado no register.html)
    const registerForm = document.getElementById('register-form');
    if (registerForm) {
        registerForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            fetch('/api/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, email, password })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    document.getElementById('register-message').innerText = data.message;
                    setTimeout(() => window.location.href = '/login', 1500);
                } else {
                    document.getElementById('register-message').innerText = data.error || 'Erro no registro.';
                }
            })
            .catch(error => console.error('Erro:', error));
        });
    }
