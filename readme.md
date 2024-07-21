NEET 2024 Marks Scrapping

To instantly connect with database-
unzip- data.zip 

# Start a postgress server using docker - you need to stay outside of the extracted zip.

docker run --name neetScam -e POSTGRES_PASSWORD=deepak -e POSTGRES_USER=deepak -e POSTGRES_DB=neetScam -d -p 5438:5432 -v "$PWD/data:/var/lib/postgresql/data" postgres:latest

connect to the database-
docker exec -it neetScam psql -d neetScam -U deepak

query
select count(*) from neetscame
expected output - 
-> count | 2325888

1. Download pdfs- python3 downloadPdf.py
2. Convert to csv - python3 pdfToCsv.py
3. Save to postgress - python3 saveToPostgress.py


Postgress-
1. create table-
CREATE table neetscam (
    id BIGSERIAL PRIMARY KEY,
    pdf INT,
    state INT,
    city INT,
    center INT,
    marks INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

2. 
A. Start postgress container-
docker run --name neetScam -e POSTGRES_PASSWORD=deepak -e POSTGRES_USER=deepak -e POSTGRES_DB=neetScam -d -p 5436:5432 -v "$PWD/data:/var/lib/postgresql/data" postgres:latest
B. Connect to it-
docker exec -it neetScam psql -d neetScam -U deepak

3. I didnt documented the whole process most probably you have to google some of the error, mostly regarding installation of modules of python(This was my first project in python).
