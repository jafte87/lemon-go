function MovieCard({Movie}){
    function onFavorateClik(){
        alert('clicked')
    }

    return <div className="movie-card">
        <div className="movie-poster">
            <img src={movie.url} alt={movie.title} />
            <div className="movie-overlay">
                <button className="favorite-btn" onClick={onFavorateClik}>
                    <Heart />
                </button>
            </div>
            <div className="movie-info">
                <h3>{movie.title}</h3>
                 <p>{movie.release_date}</p>
            </div>
        </div>
    </div>
}

export default MovieCard
