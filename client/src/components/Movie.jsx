import { Component, React } from "react"

class Movie extends Component {
    constructor(props) {
        super(props)

        this.state = {
            shortDescription: null
        }
    }

    componentDidMount() {
        this.getShortDescription()
    }

    getShortDescription = () => {
        if (this.props.description.length < 100) {
            this.setState(
                { shortDescription: this.props.description }
            )
        } else {
            let shortDescription = this.props.description.slice(0, 100) + '...'

            this.setState(
                { shortDescription: shortDescription }
            )
        }
    }

    render() {
        return (
            <div className="movie movies__movie">
                <h2 className="movie__title">{this.props.title}, {this.props.year}</h2>
                <p className="movie__description">{this.state.shortDescription}</p>
            </div>
        )
    }
}

export default Movie