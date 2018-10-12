use lead_gen_business;

SELECT clients.first_name, clients.last_name  FROM clients
JOIN sites ON sites.client_id = clients.client_id
JOIN leads ON sites.site_id = leads2.site_id;

select * from clients;

select * from sites;

select * from leads;

#Golden Query
SELECT clients.first_name, clients.last_name, COUNT(*) as total_leads from leads
JOIN sites ON leads.site_id = sites.site_id
JOIN clients ON sites.client_id = clients.client_id
GROUP BY clients.client_id
ORDER BY total_leads DESC;

#Golden Range Query
SELECT clients.first_name, clients.last_name, COUNT(*) as total_leads from leads
JOIN sites ON leads.site_id = sites.site_id
JOIN clients ON sites.client_id = clients.client_id
WHERE leads.registered_datetime BETWEEN "2011-08-01" AND "2011-08-31"
GROUP BY clients.client_id
ORDER BY total_leads DESC;

#Checking the results
SELECT *  from leads
JOIN sites ON leads.site_id = sites.site_id
JOIN clients ON sites.client_id = clients.client_id;

SELECT *  from leads
JOIN sites ON leads.site_id = sites.site_id
JOIN clients ON sites.client_id = clients.client_id
WHERE leads.registered_datetime BETWEEN "2011-08-01" AND "2011-08-31";






SELECT clients.first_name, clients.last_name  FROM clients;

SELECT *  FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
ORDER BY clients.client_id, leads.site_id;


SELECT clients.first_name, clients.last_name, COUNT(*) as total_leads from leads JOIN sites ON leads.site_id = sites.site_id JOIN clients ON sites.client_id = clients.client_id WHERE leads.registered_datetime BETWEEN '2011-10-01' AND '2012-10-01' GROUP BY clients.client_id ORDER BY total_leads DESC;