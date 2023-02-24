import './Socials.css'

function Socials(props) {
    let { socials } = props

    return (
        <div className={`socials ${props.elName}`}>
            {socials.map(social => {
                return <a key={social.id} href={social.link} className="socials__social-link"> {social.name} </a>
            })}
        </div>
    )
}

export default Socials