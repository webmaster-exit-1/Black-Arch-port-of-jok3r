# Metasploit Database Setup

## Overview

Metasploit Framework uses PostgreSQL for storing scan results, credentials, loot, and other data. This setup configures a PostgreSQL database with default credentials that can be changed by the end user.

## Default Credentials

**⚠️ IMPORTANT: Change these default credentials for production use!**

- **Database:** `msf`
- **Username:** `msf`
- **Password:** `msf_password`
- **Host:** `localhost`
- **Port:** `5432`

## Automatic Setup

The database is automatically configured when you install Metasploit via Jok3r:

```bash
python3 jok3r.py toolbox --install metasploit
```

This will:
1. Install Metasploit and PostgreSQL
2. Initialize the PostgreSQL database
3. Create the `msf` database and user
4. Configure Metasploit to use the database
5. Initialize the database schema

## Manual Setup

If you need to set up the database manually:

```bash
bash scripts/setup-metasploit-db.sh
```

### Custom Credentials

To use custom credentials during setup, set environment variables:

```bash
export MSF_DB_NAME=my_msf_db
export MSF_DB_USER=my_user
export MSF_DB_PASS=my_secure_password
bash scripts/setup-metasploit-db.sh
```

## Changing Credentials

### After Initial Setup

1. **Change the PostgreSQL password:**

```bash
sudo -u postgres psql
```

Then in the PostgreSQL prompt:

```sql
ALTER USER msf WITH PASSWORD 'your_new_secure_password';
\q
```

2. **Update Metasploit configuration:**

Edit `~/.msf4/database.yml`:

```yaml
production:
  adapter: postgresql
  database: msf
  username: msf
  password: your_new_secure_password  # Update this line
  host: localhost
  port: 5432
  pool: 5
  timeout: 5
```

3. **Restart msfconsole:**

```bash
msfconsole
```

## Verifying the Connection

Check if Metasploit is connected to the database:

```bash
msfconsole -q -x 'db_status; exit'
```

You should see:
```
[*] Connected to msf @ localhost:5432
```

## Troubleshooting

### Database Connection Failed

If you see "Database connection isn't established", try:

1. **Check PostgreSQL is running:**

```bash
sudo systemctl status postgresql
# or
sudo systemctl start postgresql
```

2. **Verify database exists:**

```bash
sudo -u postgres psql -l | grep msf
```

3. **Test connection manually:**

```bash
psql -U msf -d msf -h localhost
# Enter password when prompted
```

### Permission Denied

If you get permission errors:

```bash
sudo -u postgres psql -d msf -c "GRANT ALL ON SCHEMA public TO msf;"
```

### Reinitialize Database

To completely reset the database:

```bash
sudo -u postgres psql -c "DROP DATABASE IF EXISTS msf;"
sudo -u postgres psql -c "DROP USER IF EXISTS msf;"
bash scripts/setup-metasploit-db.sh
```

## Security Best Practices

1. **Change the default password immediately** after installation
2. **Use strong passwords** (at least 16 characters, mixed case, numbers, symbols)
3. **Restrict database access** to localhost only (default configuration)
4. **Keep PostgreSQL updated** via `pacman -Syu`
5. **Backup your database** regularly:

```bash
pg_dump -U msf msf > msf_backup_$(date +%Y%m%d).sql
```

## Database Location

- **Configuration:** `~/.msf4/database.yml`
- **PostgreSQL Data:** `/var/lib/postgres/data`
- **Logs:** `/var/lib/postgres/logfile`

## Additional Resources

- [Metasploit Documentation](https://docs.metasploit.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Metasploit Database Commands](https://www.offensive-security.com/metasploit-unleashed/using-databases/)
