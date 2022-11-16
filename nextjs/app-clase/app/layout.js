import '../styles/estilo.css';
export default function RootLayout(props) {
  return (
    <html>
      <body>
        <header>
          <div class="topnav">
            <a class="active" href="/home">
              Home
            </a>

            <a href="/contact">Contact</a>
            <a href="/about">About</a>
          </div>

          <div style={{ paddingLeft: 16 + 'px' }}>
            <h2>Top Navigation Example</h2>
            <p>Some content..</p>
          </div>
        </header>
        {props.children}
      </body>
    </html>
  );
}
