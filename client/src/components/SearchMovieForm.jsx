import { React, Component } from "react";

class SearchMovieForm extends Component {
    constructor(props) {
        super(props)
        this.state = {
            movieName: '',
            movies: null,
            filters: {}
        }
    }

    toogleFilters = e => {
        if (e) {
            e.preventDefault()
        }

        let filtersBlock = document.getElementsByClassName(
            this.props.filtersElName
        )[0]

        if (filtersBlock.style.display === 'none') {
            filtersBlock.style.display = 'block'
        } else if (filtersBlock.style.display === 'block') {
            filtersBlock.style.display = 'none'
        }
    }

    componentDidMount() {
        let filtersBlock = document.getElementsByClassName(
            this.props.filtersElName
        )[0]
        filtersBlock.style.display = 'none'
    }

    handleChange = e => {
        this.setState({
            [e.target.name]: e.target.value
        })
    }

    handleSubmit = e => {
        e.preventDefault()
        console.log(
            this.state.movieName
        )
        this.props.getMovies(
            this.state.movieName
        )
    }

    handleFilterChange = e => {
        let filters = this.state.filters
        filters[e.target.name] = e.target.value

        this.setState(
            { filters: filters }
        )
    }

    handleFilterSubmit = e => {
        e.preventDefault()

        this.props.setFilters(
            this.state.filters
        )
    }

    render() {
        return (
            <>
                <form action="" className={`search-movie-form ${this.props.elName}`}>
                    <input type="text" className="search-movie-form__form-field" name="movieName" value={this.state.moviesQuery} onChange={this.handleChange} />
                    <button className="search-movie-form__open-filters" onClick={this.toogleFilters}>Filter</button>
                    <button className="search-movie-form__button" onClick={this.handleSubmit}> Search! </button>
                </form>

                <div className={`movies-filters ${this.props.filtersElName}`}>
                    <h2 className="movies-filters__title"> Filter movies </h2>
                    <hr />
                    <div className="movies-filters__content">
                        <form className="movies-filters__form">
                            <input type="text" name="movieYearFilter" placeholder="year" className="year" onChange={this.handleFilterChange} />
                            <button className="movies-filters__submit" onClick={this.handleFilterSubmit}>Filter</button>
                        </form>
                    </div>
                </div>
            </>
        )
    }
}

export default SearchMovieForm