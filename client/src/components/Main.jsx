import { React, Component } from 'react'
import './Main.css'
import SearchMovieForm from './SearchMovieForm'
import Movies from './Movies'

class Main extends Component {
    constructor(props) {
        super(props)
        this.state = {
            movies: null,
            filters: null
        }
    }

    getMovies = moviesQuery => {
        return fetch(
            `http://127.0.0.1:8000/api/movies?search=${moviesQuery}`,
            {
                method: 'GET',
                headers: {
                    Accept: 'application/json'
                }
            }
        )
            .then(response => response.json())
            // .then(data => {
            //     if (data.Error) {
            //         console.log('nothing found')
            //     }

            //     return data.Search
            // })
            .then(movies => this.setState({ movies: movies }))
    }

    setFilters = filters => {
        this.setState({ filters: filters })
    }

    render() {
        return (
            <main className="main">
                <SearchMovieForm
                    elName='main__search-movie-form'
                    getMovies={this.getMovies}
                    filtersElName='main__movies-filters'
                    setFilters={this.setFilters} />
                <Movies elName='main__movies'
                    getMovies={this.getMovies}
                    movies={this.state.movies}
                    isLoading={false} />
            </main>
        )
    }
}

export default Main