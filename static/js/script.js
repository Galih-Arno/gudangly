document.getElementById('search-input').addEventListener('input', function() {
    let query = this.value;
    fetch('/search?query=' + query)
    .then(response => response.json())
    .then(data => {
        let tableBody = document.querySelector('table tbody');
        tableBody.innerHTML = '';
        if (data.length > 0) {
            data.forEach(item => {
                let row = `
                <tr>
                    <td>${item.id}</td>
                    <td>${item.nama_barang}</td>
                    <td>${item.kategori}</td>
                    <td>${item.stok}</td>
                    <td><a href="/edit/${item.id}" class="btn btn-warning btn-sm">Edit</a></td>
                </tr>
                `;
                tableBody.innerHTML += row;
            });
        } else {
            tableBody.innerHTML = `<tr><td colspan="5" class="text-center">Barang tidak ditemukan</td></tr>`;
        }
    });
});
