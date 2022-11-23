import '../styles/globals.css'
import {Navigation} from './components/Navigation.jsx'

export default function RootLayout({ children }) {
  return (
    <html>
      <head />
      <title>poke.next</title>
      <body>
        <Navigation />
        {children}</body>
    </html>
  )
}
