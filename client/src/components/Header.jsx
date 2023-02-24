import './Header.css'

function Header() {
    return (
        <header className="header root__header">
            <div className="header__titles-wrapper">
                <h1 className="header__title"> Movies </h1>
                <p className="header__subtitle"> Simple portfolio project </p>
            </div>
            <nav className="nav header__nav"></nav>
        </header>
    )
}

export default Header