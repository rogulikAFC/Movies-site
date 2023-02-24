import { Component } from "react";

class MovieViewer extends Component {
    constructor(props) {
        super(props)

        this.state = {}
    }

    render() {
        return (
            <div className={`movie-viewer ${this.props.elName}`}>
                <h1 className="movie-viewer__title">{this.props.title}, {this.props.year}</h1>
                <div className="info-wrapper movie-viewer__info-wrapper">
                    <table className="info-table info-wrapper__info-table">
                        <tr className="info-table__year">
                            <th>Year</th>
                            <th>{this.props.year}</th>
                        </tr>
                    </table>
                </div>
            </div>
        )
    }
}

export default MovieViewer