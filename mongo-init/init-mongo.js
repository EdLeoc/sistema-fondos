db = db.getSiblingDB('btg_db');

db.products.insertMany([
    { id: "1", name: "FPV_BTG_PACTUAL_RECAUDADORA", min_amount: 75000, category: "FPV" },
    { id: "2", name: "FPV_BTG_PACTUAL_ECOPETROL", min_amount: 125000, category: "FPV" },
    { id: "3", name: "DEUDAPRIVADA", min_amount: 50000, category: "FIC" },
    { id: "4", name: "FDO-ACCIONES", min_amount: 250000, category: "FIC" },
    { id: "5", name: "FPV_BTG_PACTUAL_DINAMICA", min_amount: 100000, category: "FPV" }
]);

db.clients.insertMany([
    { id: "1", name: "David", last_name:"León", city:"Popayán", email:"leoc@unicauca.edu.co", phone:"+573217122265", balance:500000 },
]);
