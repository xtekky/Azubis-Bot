

sign = (data, _input, ts) => {
    const _split  = aaaa(data);
    let encrypted = encryptDecrypt(_split[0] + 'i');
    let sig       = 'az' + Settlement.base64_encode(encrypted);
    // let ts        = Date.now() / 1e3 | 0

    return data + '&s=' + sig + "&s2=" + setimeout(_input) + "&s3=" + setIntervaller(_input + ts) + "&s4=" + ts + "&sc=" + t() 
}

init = () => {
    let encrypted = encryptDecrypt("undefined" + 'i');
    let sig       = 'az' + Settlement.base64_encode(encrypted);
    let ts        = Date.now() / 1e3 | 0
    return "undefined" + '&s=' + sig + "&s2=" + setimeout("unedfined") + "&s3=" + setIntervaller("undefined" + ts) + "&s4=" + ts + "&sc=" + t() 
}

