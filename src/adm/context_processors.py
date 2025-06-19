def created_by(request):
    """
    Returns author and copyright information to templates.
    """
    return {
        'CREATED_BY': 'Created by Maximilián Barjak Malček\n'
                      'Copyright &copy; 2025, All Rights Reserved'
    }
