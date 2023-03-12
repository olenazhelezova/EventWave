const deleteEntry = (id) => {
    const elt = document.getElementById('confirm-delete-modal');
    const modal = new bootstrap.Modal(elt);
    
    modal.show();    
    handler = () => {
        fetch('/api/orders/' + id, {method: 'DELETE'})
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
    fetch('/api/orders/' + id)
        .then((response) => response.json())
        .then((data) => {
            if (data.message) {
                alert(data.message)
            }

            entryModal((entryModal) => {
                // Form preparation
                entryModal.querySelector('#entity-data-modal-label').innerText = "Edit order " + id;
                document.getElementById('event_date').readOnly = true;
                document.getElementById('event_date').value = data.event.date;
                
                
                let option = document.createElement('option');
                option.value = data.event.id;
                option.innerText = data.event.name + " " + data.event.time;
                document.getElementById('event_id').appendChild(option)
                document.getElementById('event_id').value = data.event.id;
                document.getElementById('event_id').disabled = true;

                for (property in data) {
                    const field = entryModal.querySelector(`input[name=${property}]`);
                    // console.log(field)
                    if (! field) {
                        continue;
                    }
                    field.value = data[property];
                }
            }, (event) => {
                    let form = event.currentTarget.closest('.modal').querySelector('form');
                    let payload = Object.fromEntries(new FormData(form))
                    let headers = {
                        'Content-type': 'application/json; charset=UTF-8'
                    };
                    return fetch('/api/orders/' + id, {method: "PUT", body: JSON.stringify(payload), headers: headers});
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
        saveHandler(e)
        .then((response) => response.json())
        .then((data) => {
            if (data.message) {
                alert(data.message)
            }})
        .finally(() => {
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
        entryModal.querySelector('#entity-data-modal-label').innerText = "Create order";
        document.getElementById('event_date').readOnly = false;
        document.getElementById('event_id').disabled = false;

        for (field of entryModal.querySelectorAll('form input')) {
            field.value = '';
        }
        entryModal.querySelector('#event_date').value = '';
        document.getElementById('event_id').replaceChildren()
        entryModal.querySelector('#order_date').valueAsDate = new Date()
    }, (event) => {
        let form = event.currentTarget.closest('.modal').querySelector('form');
        let payload = Object.fromEntries(new FormData(form))
        let headers = {
            'Content-type': 'application/json; charset=UTF-8'
        };
        return fetch('/api/orders/', {method: "POST", body: JSON.stringify(payload), headers: headers});
    });
}

const filterGrid = () => {
    let from_date = document.getElementById('start').value
    let to_date = document.getElementById('end').value
    loadGrid(from_date, to_date);
}

const loadGrid = (from_date, to_date) => {
    document.querySelector('table.table tbody').replaceChildren();
    let url = '/api/orders'
    if (from_date || to_date)
        url += `?from_date=${from_date}&to_date=${to_date}`
    fetch(url)
    .then((response) => response.json())
    .then((data) => {
        if (data.message) {
            alert(data.message)
        }

        for (entity of data) {
            let total_price = entity.price*entity.qty
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${entity.event.name}, ${new Date(entity.event.date).toLocaleDateString('utc', {timeZone: 'UTC'})}</td>
                <td>${entity.price.toFixed(2)}</td>
                <td>${entity.qty}</td>
                <td>${total_price.toFixed(2)}</td>
                <td>${new Date(entity.order_date).toLocaleDateString('utc', {timeZone: 'UTC'})}</td>
                <td>${entity.customer.email}</td>
                <td>
                    <button type="button" class="btn btn-outline-primary btn-sm py-1" onclick="editEntry(${entity.id})">
                        <i class="fa fa-edit" aria-hidden="true"></i>
                    </button>
                    <button type="button" class="btn btn-outline-danger btn-sm py-1" onclick="deleteEntry(${entity.id})"><i class="fa fa-trash" aria-hidden="true"></i></button>
                </td>
            `
            document.querySelector('table.table tbody').appendChild(row)
        }
    })    
    .catch((reason) => {
        alert(reason)
    })
}
