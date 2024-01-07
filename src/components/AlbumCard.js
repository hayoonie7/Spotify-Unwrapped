const AlbumCard = ({ name, imageUrl, id }) => {
    return (
        <div className="album-box">
            <img src={imageUrl} alt="album cover" />
            <h5>{name}</h5>
        </div>
    );
}

export default AlbumCard;