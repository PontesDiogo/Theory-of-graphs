let start = null;
let goal = null;
let currentPath = null;
let paths = null;

$(document).ready(function() {
    $('#resetBtn').click(function() {
        location.reload();
    });

    $('#findPathBtn').click(function() {
        findPath();
    });

    $('#grid td').click(function() {
        const [x, y] = $(this).data('coord').split(',').map(Number);
        if (!start) {
            start = [x, y];
            $(this).addClass('selected-start');
        } else if (!goal && !$(this).hasClass('selected-start')) {
            goal = [x, y];
            $(this).addClass('selected-goal');
        }
    });

    $('#result').on('click', 'button', function() {
        const index = $(this).data('index');
        currentPath = paths[index];
        highlightPath(currentPath);
    });
});

async function findPath() {
    if (!start || !goal) {
        alert('Por favor, selecione um ponto de partida e um ponto de destino.');
        return;
    }
    
    const response = await fetch('/shortest-path', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ start, goal })
    });
    
    const data = await response.json();
    paths = data.paths;
    
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '';

    if (paths.length > 0) {
        paths.forEach((path, index) => {
            const pathText = `Opção ${index + 1}`;
            const button = document.createElement('button');
            button.textContent = pathText;
            button.dataset.index = index;
            resultDiv.appendChild(button);

            button.addEventListener('click', function() {
                currentPath = paths[index];
                highlightPath(currentPath);
            });
        });
    } else {
        resultDiv.textContent = 'Nenhuma rota encontrada.';
    }
}

function highlightPath(path) {
    $('#grid td').removeClass('path');
    path.forEach(coords => {
        const [x, y] = coords;
        $(`#grid td[data-coord="${x},${y}"]`).addClass('path');
    });
}
