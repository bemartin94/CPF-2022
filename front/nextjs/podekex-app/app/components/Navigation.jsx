import styles from './Navigation.module.css';
import Link from 'next/link';

const links= [{
  label:'Home',
  route: '/'
},{
  label:'About',
  route: '/about'
},
{
    label:'Pokemon',
    route: '/pokemon'
  }
  

]

export function Navigation () {
    return ( <header className={styles.header}>
        <nav>
        <ul className={styles.navigation}>
            {links.map(({label,route}) => (
          <li className={styles.mr10} key={route}><Link href={route}>{label} </Link></li>
        ))} </ul></nav></header>)
}