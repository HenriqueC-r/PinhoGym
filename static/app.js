const dashboardData = document.getElementById('dashboard-data');

const appData = {
    cadastros: JSON.parse(dashboardData.dataset.cadastros),
    valores: [
        Number(dashboardData.dataset.pago),
        Number(dashboardData.dataset.pendente),
        Number(dashboardData.dataset.fechado)
    ],
    clientes: [
        Number(dashboardData.dataset.clientesPago),
        Number(dashboardData.dataset.clientesPendente),
        Number(dashboardData.dataset.clientesFechado)
    ]
};

const formatarMoeda = (valor) => valor.toLocaleString('pt-BR', {
    style: 'currency',
    currency: 'BRL'
});

// BARRAS
new Chart(document.getElementById('graficoPagamentos'), {
    type: 'bar',
    data: {
        labels: ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'],
        datasets: [{
            label: 'Novos alunos',
            data: appData.cadastros
        }]
    }
});

// PIZZA
new Chart(document.getElementById('graficoPizza'), {
    type: 'doughnut',
    data: {
        labels: ['Pago', 'Pendente', 'Fechado'],
        datasets: [{
            data: appData.valores,
            backgroundColor: [
                '#27ae60', // verde (pago)
                '#f39c12', // laranja (pendente)
                '#e74c3c'  // vermelho (fechado)
            ]
        }]
    },
    options: {
        plugins: {
            tooltip: {
                callbacks: {
                    label: function(context) {
                        const clientes = appData.clientes[context.dataIndex];
                        const textoCliente = clientes === 1 ? 'Cliente' : 'Clientes';
                        return `${clientes} ${textoCliente} ${formatarMoeda(context.parsed)}`;
                    }
                }
            }
        }
    }
});
