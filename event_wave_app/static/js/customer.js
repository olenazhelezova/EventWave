const deleteEntry = (id) => {
    const elt = document.getElementById('confirm-delete-modal');
    const modal = new bootstrap.Modal(elt);
    
    modal.show();    
    handler = () => {
        fetch('/api/customers/' + id, {method: 'DELETE'})
            .then((response) => response.json())
            .then((data) => {
                if (data.message) {
                    alert(data.message)
                }
                loadGrid()
            }).catch(() => {
                alert('Ooops! Check your internet connection!'); 
            })
            .finally(() => modal.toggle())
    }

    let deleteButton = document.getElementById('confirm-delete-button');
    deleteButton.addEventListener('click', handler)
    elt.addEventListener('hide.bs.modal', () => {deleteButton.removeEventListener('click', handler)});
}

const editEntry = (id) => {
    fetch('/api/customers/' + id)
        .then((response) => response.json())
        .then((data) => {
            if (data.message) {
                alert(data.message)
            }

            entryModal((entryModal) => {
                // Form preparation
                entryModal.querySelector('#entity-data-modal-label').innerText = "Edit customer " + id;
                for (property in data) {
                    const field = entryModal.querySelector(`input[name=${property}]`);

                    if (! field) {
                        continue;
                    }

                    field.value = data[property];
                }
                const orders = document.getElementById('last-orders');
                if (orders) orders.remove();
                const lastOrders = document.createElement('div');
                lastOrders.id = 'last-orders';
                if (data.orders && data.orders.length > 0) {
                    let sortedOrders = data.orders.sort((a, b) => new Date(b.order_date) - new Date(a.order_date));
                    let tableHTML = `<div><h4>Previous Orders</h4><table style="width: 100%;"><thead><tr><th>Name</th>
                    <th>Order Date</th><th>Qty</th><th>Price</th><th>Total price</th></tr></thead><tbody>`;
                    sortedOrders.forEach((order) => {
                        let totalPrice = order.qty*order.price
                        tableHTML += `<tr><td>${order.event.name}</td>
                        <td>${new Date(order.order_date).toLocaleDateString('utc', {timeZone: 'UTC'})}</td>
                        <td>${order.qty}</td><td>${order.price.toFixed(2)}</td><td>${totalPrice.toFixed(2)}</td></tr>`;
                    });
                    tableHTML += '</tbody></table>';
                    lastOrders.innerHTML = tableHTML;
                } else {
                    lastOrders.innerHTML = 'No previous orders found.'
                };
                const existingElement = document.querySelector('form');
                existingElement.appendChild(lastOrders);
            }, (event) => {
                    let form = event.currentTarget.closest('.modal').querySelector('form');
                    let payload = Object.fromEntries(new FormData(form))
                    let headers = {
                        'Content-type': 'application/json; charset=UTF-8'
                    };
                    return fetch('/api/customers/' + id, {method: "PUT", body: JSON.stringify(payload), headers: headers});
                })
        })
        .catch((e) => {alert(e)})
}

const entryModal = (prepareFormHandler, saveHandler) => {
    const elt = document.getElementById('entity-data-modal');
    prepareFormHandler(elt)

    const modal = new bootstrap.Modal(elt);

    modal.show();
    handler = (e) => { 
        e.preventDefault(); 
        saveHandler(e).finally(() => {
            modal.hide();
            loadGrid()
        })
    }
    let saveButton = document.getElementById('save-entity-button');
    saveButton.addEventListener('click', handler);
    elt.addEventListener('hide.bs.modal', () => {saveButton.removeEventListener('click', handler)});
}

const addEntry = () => {
    entryModal((entryModal) => {
        entryModal.querySelector('#entity-data-modal-label').innerText = "Create customer";
        for (field of entryModal.querySelectorAll('form input')) {
            field.value = '';
            const orders = document.getElementById('last-orders');
            if (orders) orders.remove();
        }
    }, (event) => {
        let form = event.currentTarget.closest('.modal').querySelector('form');
        let payload = Object.fromEntries(new FormData(form))
        let headers = {
            'Content-type': 'application/json; charset=UTF-8'
        };
        return fetch('/api/customers/', {method: "POST", body: JSON.stringify(payload), headers: headers});
    });
}

const loadGrid = () => {
    document.querySelector('table.table tbody').replaceChildren();
    fetch('/api/customers')
    .then((response) => response.json())
    .then((data) => {
        if (data.message) {
            alert(data.message)
        }

        for (customer of data) {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${customer.name}</td>
                <td>${customer.phone_number}</td>
                <td>${customer.email}</td>
                <td>
                    <button type="button" class="btn btn-outline-primary btn-sm py-1" onclick="editEntry(${customer.id})">
                        <i class="fa fa-edit" aria-hidden="true"></i>
                    </button>
                    <button type="button" class="btn btn-outline-danger btn-sm py-1" onclick="deleteEntry(${customer.id})"><i class="fa fa-trash" aria-hidden="true"></i></button>
                </td>
            `
            document.querySelector('table.table tbody').appendChild(row)
        }
    })    
    .catch((reason) => {
        alert(reason)
    })
}
