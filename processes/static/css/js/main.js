document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const dataList = document.getElementById('data-list');

    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch('/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });
                const result = await response.json();

                if (response.ok) {
                    window.location.href = '/';
                } else {
                    document.getElementById('error-message').textContent = result.message;
                }
            } catch (error) {
                console.error('Error:', error);
            }
        });
    }

    if (dataList) {
        // Fetch data for the data view page
        fetch('/api/changes')
            .then(response => response.json())
            .then(data => {
                data.forEach(item => {
                    const li = document.createElement('li');
                    li.textContent = `${item.change_id}: ${item.description} (${item.status})`;
                    dataList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }
});
