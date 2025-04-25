const { Client } = require('pg');

const client = new Client({
  host: 'my-postgres',
  user: 'postgres',
  password: 'newpassword',
  database: 'mydb',
});

client.connect()
  .then(() => {
    console.log('✅ Connected to PostgreSQL');
    return client.query('SELECT NOW()');
  })
  .then(res => {
    console.log('🕒 Server time:', res.rows[0]);
    client.end();
  })
  .catch(err => {
    console.error('❌ Error connecting to DB:', err);
  });

