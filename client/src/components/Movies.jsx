import { Component, React } from "react"
import Movie from "./Movie"

class Movies extends Component {
    constructor(props) {
        super(props)
        this.state = {
            movies: props.movies,
            loading: false
        }
    }

    toggleLoadStatus = () => {
        this.setState({
            loading: !this.state.loading
        })
    }

    render() {
        return (
            this.state.loading ? <h2 className="preloader">Loading...</h2>
                : <div className={`movies ${this.props.elName}`}>
                    {this.props.movies ? this.props.movies.map(movie => (
                        <Movie
                            title={movie.title}
                            year={movie.year}
                            key={movie.id}
                            description={movie.description} />
                    )) : (
                        <div className="movies__no-movies">
                            <h1 className="no-movies-title"> No movies </h1>
                        </div>
                    )}
                </div>
        )
    }
}

export default Movies