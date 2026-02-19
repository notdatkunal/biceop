# Starting the Application with Docker

- Build and start the services:
   ```bash
   docker-compose up --build
   ```

## Alternative Commands

### Start in detached mode (background):
```bash
docker-compose up -d --build
```

### Stop the services:
```bash
docker-compose down
```

### View logs:
```bash
# View all logs
docker-compose logs

# View web app logs
docker-compose logs web

# View database logs
docker-compose logs db

# Follow logs in real-time
docker-compose logs -f
```

 
- Stop all containers:
   ```bash
   docker-compose down
   ```

- Remove volumes (this will delete database data):
   ```bash
   docker-compose down -v
   ```
### Rebuild after code changes:
- Rebuild and start:
   ```bash
   docker-compose up --build
   ```