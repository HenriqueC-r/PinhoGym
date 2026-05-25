// BARRAS
new Chart(document.getElementById('graficoPagamentos'), {
    type: 'bar',
    data: {
        labels: ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'],
        datasets: [{
            label: 'Novos alunos',
            data: window.appData.cadastros
        }]
    }
});

// PIZZA
new Chart(document.getElementById('graficoPizza'), {
    type: 'doughnut',
    data: {
        labels: ['Pago', 'Pendente', 'Fechado'],
        datasets: [{
            data: [window.appData.pago, window.appData.pendente, window.appData.fechado],
            backgroundColor: [
                '#27ae60', // verde (pago)
                '#f39c12', // laranja (pendente)
                '#e74c3c'  // vermelho (fechado)
            ]
        }]
    }
});