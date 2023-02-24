import './Footer.css'
import Socials from './Socials'

function Footer() {
    return (
        <footer className="footer root__footer">
            <Socials elName="footer__socials"
                socials={
                    [
                        { 'name': 'Instagram', 'link': '.', 'id': '1231352334' },
                        { 'name': 'VK', 'link': '.', 'id': '574920498' },
                        { 'name': 'Telegram', 'link': '.', 'id': 'afd3fa' },
                        { 'name': 'Pinterest', 'link': '.', 'id': '124324234' }
                    ]
                }
            />

            <div className="footer__company-info">
                <p className="footer__reg-date"> © 2023 - 2023, Movies </p>
            </div>
        </footer>
    )
}

export default Footer