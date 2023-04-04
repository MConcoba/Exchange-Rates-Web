const respose = {
  base: 'USD',
  end_date: '2023-02-09',
  rates: {
    '2023-02-06': {
      GTQ: 7.84737,
      JPY: 132.626495,
    },
    '2023-02-07': {
      GTQ: 7.838025,
      JPY: 131.046501,
    },
    '2023-02-08': {
      GTQ: 7.839479,
      JPY: 131.378504,
    },
    '2023-02-09': {
      GTQ: 7.837324,
      JPY: 131.520168,
    },
  },
  start_date: '2023-02-06',
  success: true,
  timeseries: true,
};

const datos = [
  {
    fecha: '2023-02-06',
    monedas: [
      {
        iso: 'JPY',
        pais: 'Japan',
        valor: 132.626495,
      },
      {
        iso: 'GTQ',
        pais: 'Guatemala',
        valor: 7.84737,
      },
    ],
  },
  {
    fecha: '2023-02-07',
    monedas: [
      {
        iso: 'JPY',
        pais: 'Japan',
        valor: 132.626495,
      },
      {
        iso: 'GTQ',
        pais: 'Guatemala',
        valor: 7.84737,
      },
    ],
  },
];

// ______________________________________________________________________________

const symbos = {
  success: true,
  symbols: {
    AED: 'United Arab Emirates Dirham',
    AFN: 'Afghan Afghani',
    ALL: 'Albanian Lek',
    AMD: 'Armenian Dram',
    ANG: 'Netherlands Antillean Guilder',
    AOA: 'Angolan Kwanza',
    ARS: 'Argentine Peso',
    AUD: 'Australian Dollar',
    AWG: 'Aruban Florin',
    AZN: 'Azerbaijani Manat',
  },
};

const monedas = [
  {
    value: 'AED',
    label: 'United Arab Emirates Dirham',
  },
  {
    value: 'AFN',
    label: 'Afghan Afghani',
  },
];
